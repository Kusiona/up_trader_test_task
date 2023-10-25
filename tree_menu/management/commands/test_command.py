from django.core.management.base import BaseCommand
from tree_menu.models import TableSection


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
        # first_parent = TableSection(
        #     title='first_parent'
        # )
        # first_parent_first_child = TableSection(
        #     title='first_parent_first_child',
        #     parent_section=first_parent
        # )
        # first_parent_second_child = TableSection(
        #     title='first_parent_second_child',
        #     parent_section=first_parent
        # )
        # first_parent_third_child = TableSection(
        #     title='first_parent_third_child',
        #     parent_section=first_parent
        # )
        # second_parent = TableSection(
        #     title='second_parent'
        # )
        # second_parent_first_child = TableSection(
        #     title='second_parent_first_child',
        #     parent_section=second_parent
        # )
        # second_parent_second_child = TableSection(
        #     title='second_parent_second_child',
        #     parent_section=second_parent
        # )
        # second_parent_third_child = TableSection(
        #     title='second_parent_third_child',
        #     parent_section=second_parent
        # )
        # first_parent.save()
        # first_parent_first_child.save()
        # first_parent_second_child.save()
        # first_parent_third_child.save()
        # second_parent.save()
        # second_parent_first_child.save()
        # second_parent_second_child.save()
        # second_parent_third_child.save()

        # print([section.title for section in TableSection.objects.get(parent_section__isnull=True).child_sections.all()])
