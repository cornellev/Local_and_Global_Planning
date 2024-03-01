// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#pragma once

#include <cstddef>
#include <queue>
#include <SDL.h>
#include "util/logger.h"
#include "view.h"

/** A wrapper around an SDL window. */
class Window {
    /** The dimensions of the window. */
    SDL_Rect dimensions;

    /** The SDL window. */
    SDL_Window* window;

    /** The renderer for the window. */
    SDL_Renderer* renderer;

    /** The view currently attached to the window. */
    View* view;

public:
    /** Initializes SDL and constructs a new window with the given `name`,
     * `width`, and `height`.
     *
     * @param name The name of the window.
     */
    Window(std::string name, size_t width, size_t height);

    ~Window();

    /**
     * Attaches `view` to the current window, passing memory ownership.
     *
     * Requires: `view` is non-null.
     */
    void attach_view(View* view);

    /**
     * Presents the view.
     *
     * Requires: A view has been attached with `attach_view`.
     */
    void present();

    /** Invokes `SDL_Delay` with the given milliseconds delay `ms`. */
    void delay(uint32_t ms);

    /** Returns the window frame as an `SDL_Rect`. */
    const SDL_Rect* frame() const;
};
