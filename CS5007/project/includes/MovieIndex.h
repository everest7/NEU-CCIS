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

#ifndef MOVIEINDEX_H
#define MOVIEINDEX_H

#include "htll/Hashtable.h"
#include "htll/LinkedList.h"
#include "Movie.h"
#include "MovieSet.h"


/**
 * An index is a hashtable where they key is a MovieId (Movie->Id),
 * and the value is a MovieSet.
 *
 * The Index is designed to allow indexing by one of multiple fields.
 */
typedef struct index {
  /**
   * The hashtable that takes care of the indexing of a given movie. 
   */
  Hashtable ht;
  /**
   * Since a movie struct might appear in the hashtable/index multiple times,
   * we'll keep a reference around to the list of movies for freeing.
   * 
   */
  LinkedList movies; 
} *Index; 

/**
 *  Indexes a given movie.
 *  Does not use to movie struct for anything other than
 *   extracting out the information; the movie is safe to
 *   free after calling this method.
 *
 *  \param index the index to add the movie to.
 *  \param movie a Movie to be added to the index.
 *  \param field which Movie field to index on.
 *
 *  \return 0 if successful.
 */
int AddMovieToIndex(Index index, Movie *movie, enum IndexField field);

/**
 * If this Index is indexing by movie title rather than
 * one of the fields covered in AddMovieToIndex, use this
 * function to iterate through all words in the title and
 * add them to the index.
 *
 * INPUT:
 *  index: the index to add the movie to.
 *  movie: a Movie to be added to the index.
 *
 *  \return 0 if successful.
 */
int AddMovieTitleToIndex(Index index, Movie *movie, uint64_t docId, int row);



/**
 * Gets a MovieSet for a given word from the supplied index.
 *
 * INPUT:
 *  index: the index to search
 *  term: the term to search for in the index.
 *
 *  \return A MovieSet. Returns NULL if the term is not in the index.
 *    (that is, there are no movies with the given word in the title)
 *
 */
MovieSet GetMovieSet(Index index, const char *term);

/**
 *
 *  Destroys the supplied index, freeing up all
 *   resources used by this index.
 * (value is a SetOfMovies)
 *
 */
int DestroyTypeIndex(Index index);

/**
 *
 * (value is a MovieSet)
 */
int DestroyOffsetIndex(Index index);

/**
 * Creates a new Index. Allocates all the memory
 *  necessary for this index.
 *
 */
Index CreateIndex();

/**
 * Helper function to compute the key from a string, given
 * a Movie and which field is to be used as the key.
 *
 * \return uint64_t to be used as a key in the MovieIndex.
 */
uint64_t ComputeKey(Movie* movie, enum IndexField);

#endif
