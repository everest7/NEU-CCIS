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

#ifndef QUERYPROCESSOR_H
#define QUERYPROCESSOR_H

#include "MovieIndex.h"
#include "DocIdMap.h"

/**
 *  A SearchResult is a doc_idd and row_id,
 * representing a particular row in a particular file.
 *
 */
typedef struct searchResult {
  uint64_t doc_id;
  int row_id;
} *SearchResult;

/**
 * A SearchResultIter goes through every element in the hashtable,
 * which are all lists of document locations.
 *
 */
typedef struct searchResultIter {
  int cur_doc_id;
  HTIter doc_iter;
  LLIter offset_iter;
  int numResults;
} *SearchResultIter;

SearchResultIter CreateSearchResultIter(MovieSet set);

void DestroySearchResultIter(SearchResultIter iter);

/**
 * Returns the number of elements in the provided SearchResultIter.
 * This is the number of search results.
 *
 */
int NumResultsInIter(SearchResultIter iter);

int SearchResultGet(SearchResultIter iter, SearchResult output);

int SearchResultNext(SearchResultIter iter);

int SearchResultIterHasMore(SearchResultIter iter);

SearchResultIter FindMovies(Index index, char *term);

/**
 * Opens the file specified by the SearchResult as named
 *  in the DocIdMap and writes the specified row to the dest.
 *
 * INPUT:
 *    result: A SearchResult that contains a docId and rowId
 *     docIds: The DocIdMap that contains the doc names specified in result.
 *     dest: A pointer to a char array where the row from the given file and row should be written.
 *
 * RETURNS:
 *     0 if successful; Not 0 if failed.
 */
int CopyRowFromFile(SearchResult result, DocIdMap docIds, char *dest);


#endif
