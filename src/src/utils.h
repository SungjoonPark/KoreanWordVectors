/**
 * Copyright (c) 2016-present, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#ifndef FASTTEXT_UTILS_H
#define FASTTEXT_UTILS_H

#include <fstream>

#if defined(__clang__) || defined(__GNUC__)
# define FASTTEXT_DEPRECATED(msg) __attribute__((__deprecated__(msg)))
#elif defined(_MSC_VER)
# define FASTTEXT_DEPRECATED(msg) __declspec(deprecated(msg))
#else
# define FASTTEXT_DEPRECATED(msg)
#endif

namespace fasttext {

namespace utils {

  int64_t size(std::ifstream&);
  void seek(std::ifstream&, int64_t);
}

}

#endif
