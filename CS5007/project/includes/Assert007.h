#ifndef _A6_ASSERT007_H_
#define _A6_ASSERT007_H_

// A wrapper for assert that permits side-effects within the
// Assert007() statement.  Borrowed from:
//
//   http://www.acm.uiuc.edu/sigops/roll_your_own/2.a.html

void AssertionFailure(const char *exp, const char *file,
                      const char *basefile, int line);

#define Assert007(exp) if (exp) ; \
  else AssertionFailure(#exp, __FILE__, __BASE_FILE__, __LINE__)

#endif  // _a6_ASSERT007_H_
