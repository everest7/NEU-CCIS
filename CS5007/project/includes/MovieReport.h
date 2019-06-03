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

#include <stdio.h>
#include <stdlib.h>

#include "MovieIndex.h"
#include "MovieSet.h"

#ifndef MOVIEREPORT_H
#define MOVIEREPORT_H

/**
 * MovieReport contains functions to generate and write out a report
 * of movies, based on an indexed set of movies (that is, and Index).
 */

/**
 * Prints a report to the terminal, given an index of movies.
 */
void PrintReport(Index index);

/**
 * Helper function; Prints just the movies in a set.
 *
 */
void OutputMovieSet(LinkedList movies, char* desc);

/**
 * Writes the report to the specified output FILE.
 */
void OutputReport(Index index, FILE* output);


/*
 * Writes the report to the specified output.
 */
void SaveReport(Index index, char* filename);

#endif   // MOVIEREPORT_H
