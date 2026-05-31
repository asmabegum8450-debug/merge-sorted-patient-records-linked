class ListNode:
    def __init__(self, ssn, age=None, full_name=None):
        self.ssn = ssn
        self.age = age
        self.full_name = full_name
        self.next = None


def merge_patient_records(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.ssn <= list2.ssn:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


def build_linked_list(records):
    dummy = ListNode(0)
    current = dummy

    for ssn, age, full_name in records:
        current.next = ListNode(ssn, age, full_name)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append((head.ssn, head.age, head.full_name))
        head = head.next

    return result
