from django import template
from menu.models import Menu
from django.db.models import Prefetch

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    menu = Menu.objects.prefetch_related(
        Prefetch('items')
    ).filter(name=menu_name).first()

    if not menu:
        return {'menu_items': []}

    all_items = list(menu.items.all())
    active_item = next((item for item in all_items if item.get_absolute_url() == current_path), None)

    def get_active_branch(item):
        branch = set()
        while item:
            branch.add(item.id)
            item = item.parent
        return branch

    active_branch = get_active_branch(active_item) if active_item else set()

    def build_tree(parent=None, level=0):
        result = []
        for item in all_items:
            if item.parent_id == (parent.id if parent else None):
                children = build_tree(item, level + 1)
                result.append({
                    'item': item,
                    'children': children,
                    'is_active': item.id in active_branch,
                    'level': level,
                })
        return result

    return {'menu_items': build_tree()}
