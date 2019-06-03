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
#ifndef FILECRAWLER_H
#define FILECRAWLER_H


#include "DocIdMap.h"
#include "htll/LinkedList.h"


/**
 * Iterates through a given directory, and for all files it
 * finds, adds them to the provided DocIdMap to assign a unique
 * id.
 *
 * The result of this function is a DocIdMap that contains all the files
 * we will want to index and search.
 *
 * \param dir which directory to crawl
 * \param map the DocIdMap to put the filenames in.
 */
void CrawlFilesToMap(const char *dir, DocIdMap map);


#endif  // FILECRAWLER_H
