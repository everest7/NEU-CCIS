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

#ifndef FILEPARSER_H
#define FILEPARSER_H

#include "MovieIndex.h"
#include "DocIdMap.h"
#include "htll/LinkedList.h"


/**
 * Given a map of all the files that we want to index
 * and search, open each file and index the contents to index
 *
 * \param docs the DocIdMap that contains all the files we want to parse.
 * \param the index to hold all the indexed docs.
 */
int ParseTheFiles(DocIdMap docs, Index index);


int GetRowFromFile(char *file, long rowId);

LinkedList ReadFile(const char* filename);

Index BuildMovieIndex(LinkedList movies, enum IndexField field_to_index);

int ParseTheFiles_MT(DocIdMap docs, Index index);

#endif
