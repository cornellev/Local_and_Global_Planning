// Copyright (C) 2024 Ethan Uppal. All rights reserved.

#include <iostream>
#include <memory>
#include "gui/window.h"
#include "sim/world_view.h"

#define WINDOW_WIDTH 700
#define WINDOW_HEIGHT 700

int main() {
    Window window("Spring Path", WINDOW_WIDTH, WINDOW_HEIGHT);

    WorldView* view = new WorldView();
    window.attach_view(view);

    window.present();
}
