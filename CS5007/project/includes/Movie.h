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

#ifndef MOVIE_H
#define MOVIE_H

#define NUM_GENRES 10

/**
 * IndexField is an enum that we use to indicate fields of Movies.
 */
enum IndexField {Genre, Year, Type, Id};

/**
 * A Movie is a struct that holds information about a Movie.
 *
 * Fields that are null or invalid are -1 for the int fields, and NULL
 * if they are pointer fields.
 *
 */
typedef struct movie {
  char *id;
  char *type;
  char *title;
  int isAdult;
  int year;
  int runtime;
  //  char *genres;  // TODO: Make this an array (or linked list) of char*s
  char *genres[NUM_GENRES];
} Movie, *MoviePtr;


/**
 *  Creates an empty movie struct.
 *
 *  Mallocs space for the fields, but initializes the fields to
 *  default/null values.
 */
Movie* CreateMovie();


/**
 * Destroys a movie, freeing up all char*s in the struct.
 */
void DestroyMovie(Movie* movie);



void DestroyMovieWrapper(void *movie);


/**
 * Given a char* that is a row in the data file,
 * Creates and populates a Movie struct accordingly.
 *
 * Expected sample row:
 * id       |type |Title1   |Title2   |IsAdult|Year|?|?|Genres
 * tt0003609|movie|Alexandra|Alexandra|0      |1915|-|-|-
 *
 * Fields are separated by a pipe (|), and a dash (-) specifies an empty value.
 *
 * Returns: A pointer to a Movie struct that has been allocated and populated.
 */
Movie* CreateMovieFromRow(char *dataRow);


void Trim(char* string);

#endif  // MOVIE
