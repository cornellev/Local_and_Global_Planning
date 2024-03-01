// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#include "keyboard.h"

Keyboard::Keyboard() {}

void Keyboard::update(const SDL_Event& key_event) {
    switch (key_event.type) {
        case SDL_KEYDOWN: {
            states[key_event.key.keysym.sym] = true;
            break;
        }
        case SDL_KEYUP: {
            states[key_event.key.keysym.sym] = false;
            break;
        }
    }
}

bool Keyboard::query(SDL_Keycode code) const {
    return states.count(code) ? states.find(code)->second : false;
}
