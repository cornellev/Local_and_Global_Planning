// Copyright (C) 2024 Ethan Uppal. All rights reserved.

#pragma once

#include "vector.h"

struct Circle {
    Circle(Vector center, double radius): center(center), radius(radius) {}
    Vector center;
    double radius;
};
