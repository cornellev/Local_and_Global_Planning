// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#pragma once

#include <SDL.h>
#include <vector>
#include "gui/view.h"
#include "util/keyboard.h"
#include "geo/path.h"
#include "geo/circle.h"

class WorldView final : public View {
    Keyboard keyboard;
    Path global;

    // TODO: need to factor into class/struct
    Path local_pos;
    Path old_local_pos;
    std::vector<double> initial_lengths;
    Path local_vel;
    Path local_acc;

    std::vector<Circle> obstacles;

    /** Draws the points along `path` and connects them with lines.
     * (`r`,`g`,`b`) is the color used. The points will be represented with
     * circles of radius `radius`. */
    void draw_path(SDL_Renderer* renderer, const Path& path, uint8_t radius,
        uint8_t r, uint8_t g, uint8_t b);

    /** Samples points along the first segment of the global path. */
    void interpolate_points();

    /** Updates the sampled points to apply forces. */
    void run_kinematics(double dtime);

public:
    /** Creates a world view for locally planning with a `global` plan and
     * dynamic `obstacles`. */
    WorldView(Path global, std::vector<Circle> obstacles);
    ~WorldView() noexcept override;

    void on_event(const SDL_Event& event) override;
    void draw(SDL_Renderer* renderer, const SDL_Rect* frame,
        double dtime) override;
};
