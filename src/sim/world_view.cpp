// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#include "util/logger.h"
#include "util/keyboard.h"
#include "world_view.h"

WorldView::WorldView() {
    setup();
}

WorldView::~WorldView() {}

void WorldView::setup() {}

void WorldView::update(double dtime) {}

void WorldView::on_event(const SDL_Event& event) {
    keyboard.update(event);
}

void WorldView::draw(SDL_Renderer* renderer, const SDL_Rect* frame,
    double dtime) {}
