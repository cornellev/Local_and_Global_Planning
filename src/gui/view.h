// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#pragma once

#include <SDL.h>

class View {
public:
    virtual ~View() = default;

    /** Handle a new `event`. Must override. */
    virtual void on_event(const SDL_Event& event) = 0;

    /**
     * Draw the view's contents to `renderer`. Must override.
     *
     * @param The window the view belongs to.
     * @param renderer The renderer for the window.
     * @param dtime The time elapsed since the view was last rendered.
     */
    virtual void draw(SDL_Renderer* renderer, const SDL_Rect* frame,
        double dtime) = 0;
};
