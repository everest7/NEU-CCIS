// CS 5007, Northeastern University, Seattle
// Summer 2017
//
// Assignment 2
#include <stdint.h>

#include "LinkedList.h"


#ifndef HASHTABLE_H
#define HASHTABLE_H

//typedef LinkedList *LinkedList_ht;

struct hashtableInfo {
	int num_buckets;
	int num_elements;
	LinkedList* buckets;
};

typedef struct hashtableInfo* Hashtable;

struct hashtableIter {
	int placeholder;
};

typedef struct hashtableIter HashtableIter;

// Hashtables store key/value pairs.  We'll define a key to be an
// unsigned 64-bit integer; it's up to the customer to figure out how
// to produce an appropriate hash key, but below we provide an
// implementation of FNV hashing to help them out.  We'll define
// a value to be a (void *), so that customers can pass in pointers to
// arbitrary structs as values, but of course we have to worry about
// memory management as a side-effect.
typedef struct {
  uint64_t   key;    // the key in the key/value pair
  void      *value;  // the value in the key/value pair
} HTKeyValue, *HTKeyValuePtr;

// When freeing a HashTable, customers need to pass a pointer to a function
// that frees the payload.  The pointed-to function is invoked once for each
// value in the HashTable.
// ValueFreeFnPtr takes in a void* as a parameter, and returns void.
typedef void(*ValueFreeFnPtr)(void *value);

// =====================

// Allocates and returns a new Hashtable.
//
// INPUT:
//   numBuckets: The number of buckets this hashtable will start with.
//
// Returns NULL if the hashtable was unable to be malloc'd, or
// the hashtable.
Hashtable CreateHashtable(int num_buckets);

// Destroys and Frees the hashtable.
//
// Input:
//   ht: the table to be free'd. It is unsafe to use the
//    hashtable after this is called.
//   value_free_function: The function to be called to free the
//     values in this hashtable.
void DestroyHashtable(Hashtable ht, ValueFreeFnPtr value_free_function);

// Puts the given key value pair int the hashtable.
//
// INPUT:
//   ht: the hashtable to insert into
//   kvp: the key-value pair to put into the hashtable.
//   old_kvp: if there is a collision, sets the old_kvp to point at the previous value. 
//
// Returns 0 if put is successful.
// Returns 1 on failure (e.g., no more memory)
// Returns 2 if the key is already in the hashtable
int PutInHashtable(Hashtable ht, HTKeyValue kvp, HTKeyValue *old_kvp);

// Looks up the given key in the hashtable.
// Returns the Key-Value pair in the provided result pointer.
//
// INPUT:
//   ht: the hashtable to lookup in
//   key: the key to lookup
//   result: If the key is in the hashtable, this is used
//      to return a pointer to a HTKeyValue to the caller.
//      Note, this HTKeyValue is still in the hashtable, so can't
//      be used to free the value.
//
// Returns 0 if the lookup was successful (and the result is valid).
// Returns -1 if the key was not found.
int LookupInHashtable(Hashtable ht, uint64_t key, HTKeyValue *result);

// Replaces the value of a given key in the hashtable.
//
// INPUT:
//   ht: Hashtable to replace value
//   key: key of item to be replaced
//   new_val: new item to put in HT
//   old_val: the HTKeyValue that was removed from the hashtable,
//      which allows the caller to free it as necessary.
//
// Returns 0 if successful (and oldVal is valid)
// Returns -1 if the key was not found in the hashtable (and oldval is invalic)
//int ReplaceInHashtable(Hashtable ht, HTKeyValue new_val, HTKeyValue *old_val);

// Gets the number of elements in the hashtable.
//
// INPUT:
//   ht: the Hashtable
//
// Returns the number of elements in the hashtable.
int NumElemsInHashtable(Hashtable ht);

// Removes the HTKeyValue with the given key from the
//  hashtable.
//
// INPUT:
//   ht: the hashtable
//   key: the key to remove
//   junkKVP: a pointer to the removed HTKeyValue, to
//     allow the value to be freed by the caller.
//
// Returns 0 if the key was found successfully (and junkKVP is valid)
// Returns -1 if the key was not found in the hashtable.
int RemoveFromHashtable(Hashtable ht, uint64_t key, HTKeyValue *junk_kvp);

// Computes an int from a string, to be used for a key in a HTKeyValue.
//
// INPUT:
//   buffer: a pointer to the array holding the string
//   len: the length of the string
//
// Returns an int to be used as an input to FNVHashInt64 for the hash value.
uint64_t FNVHash64(unsigned char *buffer, unsigned int len);

// Creates a hashed value from a given key.
//
// INPUT:
//   makehash: an int to be hashed for the key of a HTKeyValue pair
//
// Returns the int to be used as a key.
uint64_t FNVHashInt64(uint64_t makehash);



//=======================

// We can create an iterator for a hashtable, just like we can
// for a LinkedList. The iterator will go through all of the elements
// in the Hashtable, but the order is undefined; it can also vary
// from call to call.
// As with the LinkedList, any changes to the Hashtable that modify
// it while iterating makes the iterator dangerous to use, and that
// iterator should be destroyed.
struct ht_itrec;
typedef struct ht_itrec *HTIter;  // same trick to hide implementation.

// Create an iterator for a given hashtable.
// If there are elements in the hashtable, the iterator
// is initialized to point to the first. If there
// are no elements in the hashtable, it is considered an
// error and NULL is returned.
//
// INPUT:
//  ht: the hashtable to iterate over
//
// Returns NULL on failure, non-NULL on success.
HTIter CreateHashtableIterator(Hashtable table);

// Destroys and frees all resources malloc'd by this iterator.
// Call this when you are done with it.
//
// INPUT:
//  iter: the iterator to free. Do not use it after destroying it.
void DestroyHashtableIterator(HTIter iter);

// Moves to the next element in the iterator.
//
// INPUT:
//   iter: the iterator 
//
// Returns:
//
//   0 If successful
int HTIteratorNext(HTIter iter);

// Checks to see if this iterator has more elements to return.
//
// INPUT:
//  iter: the iterator to check
//
// Returns:
//  0 if there are no more elements.
int HTIteratorHasMore(HTIter iter);

// Populates dest with the element iter is currently pointing at.
//
// Returns:
//  0 if successful
// 
int HTIteratorGet(HTIter iter, HTKeyValuePtr dest); 
#endif  // HASHTABLE_H

