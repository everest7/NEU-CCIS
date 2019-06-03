/*
 *  Created by Adrienne Slaughter
 *  CS 5007 Spring 2019
 *  Northeastern University, Seattle
 *
 *  This is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  It is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  See <http://www.gnu.org/licenses/>.
 */
 #ifndef DOCIDMAP_H
#define DOCIDMAP_H

#include "htll/Hashtable.h"

//===========================
//
// A docid map connects unique IDs to files.
//
//===========================

// A wrapper to iterate through docIds.
typedef HTIter DocIdIter;

// A docId is a Hashtable, where
// the key is an int and the value
// is a filename.

/**
 * A DocIdMap is a Hashtable that maps unique IDs to filenames.
 * The key is an int, and the value is a char* that is a filename.
 *
 */
typedef Hashtable DocIdMap;


void DestroyString(void *val);


/**
 *  Creates and returns a pointer to an empty DocIdMap.
 *
 *
 *
 */
DocIdMap CreateDocIdMap();


/**
 * Wrapper to destroy DocIdMap.
 *
 * Destroys and frees all data in the docidmap.
 *
 * \param map the DocId map to destroy
 */
void DestroyDocIdMap(DocIdMap map);

/**
 * Given a map and a pointer to a filename, puts the
 * filename in the map and gives it a unique ID.
 *
 * Assumes that the filename has been malloc'd
 * prior to being added to the map.
 *
 */
void PutFileInMap(char *filename, DocIdMap map);

/**
 * Creates an iterator to go through all of the
 * document IDs in the DocIdMap.
 *
 * \param map the DocIdMap to iterate through.
 */
DocIdIter CreateDocIdIterator(DocIdMap map);

// Destroy the DocIdIterator.
void DestroyDocIdIterator(DocIdIter iter);

// Given a map and a docId, returns the relevant
// filename.
char *GetFileFromId(DocIdMap docs, int docId);


#endif
