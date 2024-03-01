// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#pragma once

#include <SDL.h>
#include "gui/view.h"
#include "util/keyboard.h"

class WorldView final : public View {
    Keyboard keyboard;

    void setup();
    void update(double dtime);

public:
    /** Creates a new world view. */
    WorldView();
    ~WorldView() noexcept override;

    void on_event(const SDL_Event& event) override;
    void draw(SDL_Renderer* renderer, const SDL_Rect* frame,
        double dtime) override;
};
