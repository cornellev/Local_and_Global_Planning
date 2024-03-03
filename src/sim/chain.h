// Copyright (C) 2024 Ethan Uppal. All rights reserved.

#pragma once

#include "geo/path.h"

class Chain {
    Path chain;

public:
    const Path& path() const;
};
