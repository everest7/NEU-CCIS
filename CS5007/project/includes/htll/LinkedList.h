// CS 5007, Northeastern University, Seattle
// Spring 2019
// Adrienne Slaughter
// 
// Inspired by UW CSE 333; used with permission. 
// 
// This is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published
//  by the Free Software Foundation, either version 3 of the License,
//  or (at your option) any later version.
// It is distributed in the hope that it will be useful, but
//  WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
//  General Public License for more details.

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

// A LinkedList is a pointer to a ll_head struct.
// To hide the implementation of LinkedList, we declare the "struct ll_head"
// structure here, but we *define* the structure in the internal header
// LinkedList_priv.h. This lets us define a pointer to LinkedList as a new
// type while leaving the implementation details opaque to the

typedef struct ll_head *LinkedList; 


// We'll use "function pointers" to help us free things easily. 
typedef void(*LLPayloadFreeFnPtr)(void *payload);

// We'll use a function pointer to compare two arbitrary structs.
typedef int(*LLPayloadComparatorFnPtr)(void *payload_a, void *payload_b);

// Doing the same trick for LLIter that we did for LinkedList
struct ll_iter;
typedef struct ll_iter *LLIter;  



// ======================================================
// LinkedList: A Doubly-Linked List 
// ======================================================

// Creates a LinkedList.
// The customer is responsible for calling DestroyLinkedList()
// to destroy and free the LinkedList when done.
//
// Returns a LinkedList; NULL if there's an error. 
LinkedList CreateLinkedList();

// Destroys a LinkedList.
// All structs associated with a LinkedList will be
// released and freed. Payload_free_function will 
// be used to free the payloads in the list. 
//
// INPUT: A pointer to a LinkedList.
// INPUT: A pointer to a function used to free the payload. 
//
// Returns 0 if the destroy was successful; non-zero for failure. 
int DestroyLinkedList(LinkedList list, LLPayloadFreeFnPtr payload_free_function);



unsigned int NumElementsInLinkedList(LinkedList list); 

// Adds an element to the head of a LinkedList, with the payload
// as the given pointer.
// The customer is responsible for allocating the payload.
//
// INPUT: A pointer to the LinkedList that will be added to,
// INPUT: A pointer to a payload for a node in the linkedList.
//
// Returns 0 if the insertion was successful; non-zero for failure. 
int InsertLinkedList(LinkedList, void*);

// Copies the pointer to the payload at the head of a list 
// to the provided dataPtr, and removes the head node from the list. 
//
// INPUT: A pointer to the LinkedList.
// INPUT: A pointer to a pointer that will be updated 
//        with the payload at the head of the list. .
//
// Returns 0 if the pop was successful; non-zero for failure. 
int PopLinkedList(LinkedList list, void** dataPtr); 

// Adds an element to the tail of a LinkedList, with the payload
// as the given pointer.
// The customer is responsible for allocating the payload.
//
// INPUT: A pointer to the LinkedList that will be added to,
// INPUT: A pointer to a payload for a node in the linkedList.
//
// Returns 0 if the insertion was successful; non-zero for failure. 
int AppendLinkedList(LinkedList list, void* payload);

// Copies the pointer to the payload at the tail of a list 
// to the provided dataPtr, and removes the tail node from the list. 
//
// INPUT: A pointer to the LinkedList.
// INPUT: A pointer to a pointer that will be updated 
//        with the payload at the tail of the list. 
//
// Returns 0 if the pop was successful; non-zero for failure. 
int SliceLinkedList(LinkedList list, void** payload);

// Sorts the list given the comparator. 
// 
// INPUT: The list to sort
// INPUT: 1 if the sort should be ascending; 0 for descending. 
// INPUT: A pointer to the function that will be used to compare two payloads. 
void SortLinkedList(LinkedList list, unsigned int ascending, LLPayloadComparatorFnPtr comparator);


// ======================================================
// LLIter: A Linked List Iterator
// ======================================================

// Creates a iterator for the given linkedList.
// It is the customer's responsibility to ensure
// that the iterator is destroyed before modifying
// the LinkedList.
// The customer also needs to call DestroyLLIter to free
// it when the customer is done.
//
// INPUT: A pointer to a LinkedList to be iterated.
LLIter CreateLLIter(LinkedList list);

// Determines if there are more elements in a given iterator.
//
// INPUT: An existing iterator.
//
// Returns 0 if there are no next elements; 1 if there are. 
int LLIterHasNext(LLIter iter);

// Determines if there are more elements in a given iterator.
//
// INPUT: An existing iterator.
//
// Returns 0 if there are no previous elements; 1 if there are. 
int LLIterHasPrev(LLIter iter);

// Steps the iterator to the next element in the LinkedList. 
//
// INPUT: A pointer to an existing iterators.
//
// Returns 0 if it was successful. 
int LLIterNext(LLIter iter);

// Steps the iterator to the previous element in the LinkedList
// if there is one. 
//
// INPUT: A pointer to an existing iterators.
//
// Returns 0 if successful; 1 otherwise. 
int LLIterPrev(LLIter iter);

// Destroys and frees the given iterator.
//
// INPUT: A 0 to an existing iterator.
//
// Returns 0 if the iterator was successfully
//   destroyed and freed.
int DestroyLLIter(LLIter iter);

// Copies the pointer to the payload of the current element 
// to the pointer specified by the argument. 
// 
// INPUT: The iterator
// INPUT: A pointer to a place to copy the payload pointer. 
// 
// Returns 0 if successful; 1 otherwise. 
int LLIterGetPayload(LLIter iter, void** payload); 

// Delete the node the iterator is pointing to.  After deletion, the iterator:
//
// - is invalid and cannot be used (but must be freed)
// - if there was only one element in the list
// - the successor of the deleted node, if there is one.
// - the predecessor of the deleted node, if the iterator was pointing at
//   the tail.
//
// INPUT:  the iterator to delete from
// INPUT: invoked to free the payload
//
// Returns:
// - 1 if the deletion succeeded, but the list is now empty
// - 0 if the deletion succeeded, and the list is still non-empty
int LLIterDelete(LLIter iter, LLPayloadFreeFnPtr payload_free_function); 


// Insert an element right before the node that the interator points
// to.  (If you want to insert at the end of a list, use
// AppendLinkedList.)
//
// INPUT: the iterator to insert through
// INPUT: the payload to insert
//
// Returns:
// 1 on failure (out of memory)
// 0 on success; the iterator still points to the same node,
//   not to the inserted node.
int LLIterInsertBefore(LLIter iter, void* payload); 

#endif  // LINKEDLIST_H


