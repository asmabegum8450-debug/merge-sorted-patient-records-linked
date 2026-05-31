# Merge Sorted Patient Records Linked List

## Problem

HealthMerge and CarePlus each have sorted linked lists of patient records.
Each record is sorted by SSN.

The goal is to merge both sorted linked lists into one sorted linked list.

If duplicate SSNs exist, both records should be kept.

## Clarifying Questions

1. Are both input lists already sorted by SSN?
2. Should duplicate SSNs be included in the final result?
3. Can either linked list be empty?
4. Should we create new nodes or reuse the existing nodes?
5. What data does each patient record contain?

## Approach

Use two pointers:

- One pointer starts at the head of HealthMerge's list.
- One pointer starts at the head of CarePlus's list.
- Compare the SSNs.
- Add the smaller SSN node to the merged list.
- Move that pointer forward.
- Continue until one list is empty.
- Attach the remaining nodes from the other list.

## Flowchart

```text
Start
 |
 v
Create dummy node
 |
 v
Are both lists non-empty?
 |
 |-- Yes --> Compare list1.ssn and list2.ssn
 |              |
 |              |-- list1.ssn <= list2.ssn --> attach list1 node
 |              |
 |              |-- otherwise --> attach list2 node
 |
 v
Move current pointer
 |
 v
Repeat until one list is empty
 |
 v
Attach remaining nodes
 |
 v
Return dummy.next
 |
 v
End
