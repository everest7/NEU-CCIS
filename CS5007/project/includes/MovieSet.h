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

#ifndef MOVIESET_H
#define MOVIESET_H

#include "htll/Hashtable.h"
#include "Movie.h"

/**
 * A MovieSet is a set of movies.
 *
 * doc_index is a hashtable where the key is a doc_id,
 * and the value is a linked list. The payloads in the linked
 * list is a row_id that indicates which row in the specified file
 * has the info about the movie that belongs in this set.
 */
typedef struct movieSet {
  char *desc; /*!< A string describing the movie set. */
  Hashtable doc_index; /*!< A hashtable that holds the info about which doc each movie is in*/
  int num_movies;
} *MovieSet;

/**
 * A SetOfMovies is a set of movies.
 *
 * The difference between MovieSet and SetOfMovies is that SetOfMovies
 * actually contains a list of populated movie structs, rather than references
 * to where the data is stored. 
 */
typedef struct setOfMovies {
  char *desc;
  LinkedList movies; 
} *SetOfMovies;

/**
 * Adds a Movie to the set.
 *
 * \param set The MovieSet to add the movie to
 * \param doc_id Which document/file the movie is stored in
 * \param row_id Which row in the file the movie can be found.
 *
 * \return 0 if successful.
 */
int AddMovieToSet(MovieSet set, uint64_t doc_id, int row_id);

/**
 * Destroys a movie set, freeing everything necessary.
 *
 * /param set the MovieSet to be destroyed.
 *
 */
void DestroyMovieSet(MovieSet set);

void DestroySetOfMovies(SetOfMovies set); 

/**
 * Prints the "offsetList" for a given set of movies .
 * The offset list is the row IDs for each movie in the set.
 * Helpful for debugging.
 *
 * \param list A linkedlist of row Ids (the value of the doc_index)
 */
void PrintOffsetList(LinkedList list);

/**
 * Determines if a MovieSet contains movies from a specifid
 * document or file.
 *
 * \param set The MovieSet to query
 * \param doc_id Which doc to look for.
 *
 * \return 0 if the doc_id is found, -1 otherwise.
 */
int MovieSetContainsDoc(MovieSet set, uint64_t doc_id);

/**
 * Creates a new, empty MovieSet given the description.
 *
 * \param desc the description of what relates the movies that will be in this MovieSet
 *
 * \return A pointer to the new MovieSet that has been allocated.
 */
MovieSet CreateMovieSet(char *desc);

/**
 * Destroys the offset lists that are the values
 * of the hashtable.
 *
 * \param val the Offset list to be destroyed.
 */
void DestroyOffsetList(void *val);

/**
 * Destroys the MovieSet.
 *
 * \param val the movieSet to be destroyed.
 */
void DestroyMovieSet(MovieSet val);



SetOfMovies CreateSetOfMovies(char *desc);

int AddMovieToSetOfMovies(SetOfMovies set, Movie *movie);

void NullFree(void *);

int NumMoviesInSet(MovieSet);


#endif
