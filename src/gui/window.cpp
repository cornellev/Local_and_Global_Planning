// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#include <cassert>
#include "window.h"

Window::Window(std::string name, size_t width, size_t height): view(nullptr) {
    dimensions.x = 0;
    dimensions.y = 0;
    dimensions.w = (int)width;
    dimensions.h = (int)height;

    if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
        Log << "SDL initialization failed: " << SDL_GetError() << '\n';
        exit(1);
    }

    window = SDL_CreateWindow(name.c_str(), SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED, width, height, SDL_WINDOW_SHOWN);
    if (!window) {
        Log << "failed to create window: " << SDL_GetError() << '\n';
        exit(1);
    }

    renderer = SDL_CreateRenderer(window, 0, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        Log << "failed to create renderer: " << SDL_GetError() << '\n';
        exit(1);
    }
}

Window::~Window() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    if (view) {
        delete view;
    }
    SDL_Quit();
}

void Window::attach_view(View* view) {
    assert(view);
    this->view = view;
}

void Window::present() {
    assert(view);
    SDL_Event event;
    bool quit_requested = false;
    Uint64 start_timestamp = SDL_GetPerformanceCounter();
    do {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit_requested = true;
                break;
            }
            view->on_event(event);
        }
        Uint64 now_timestamp = SDL_GetPerformanceCounter();
        double elapsed = (double)(now_timestamp - start_timestamp)
                         / (double)SDL_GetPerformanceFrequency();
        view->draw(renderer, frame(), elapsed);
        SDL_RenderPresent(renderer);
        start_timestamp = now_timestamp;
    } while (!quit_requested);
}

void Window::delay(uint32_t ms) {
    SDL_Delay((Uint32)ms);
}

const SDL_Rect* Window::frame() const {
    return &dimensions;
}
