// Copyright (C) 2024 Ethan Uppal. All rights reserved.

#include <iostream>
#include <memory>
#include "gui/window.h"
#include "sim/world_view.h"

#define WINDOW_WIDTH 700
#define WINDOW_HEIGHT 700

int main() {
    Window window("Spring Path", WINDOW_WIDTH, WINDOW_HEIGHT);

    Path global = {Vector(50, 50), Vector(250, 250), Vector(350, 400)};
    std::vector<Circle> obstacles = {Circle(Vector(150, 150), 50)};
    WorldView* view = new WorldView(global, obstacles);
    window.attach_view(view);

    window.present();
}
