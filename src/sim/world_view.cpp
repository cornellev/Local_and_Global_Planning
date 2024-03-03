// Copyright (C) 2023-4 Ethan Uppal. All rights reserved.

#include <cassert>
#include <cstdlib>
#include "util/logger.h"
#include "util/keyboard.h"
#include "geo/midpoint.h"
#include "world_view.h"

WorldView::WorldView(Path global, std::vector<Circle> obstacles)
    : global(global), obstacles(obstacles) {
    interpolate_points();
}

WorldView::~WorldView() {}

void WorldView::draw_path(SDL_Renderer* renderer, const Path& path,
    uint8_t radius, uint8_t r, uint8_t g, uint8_t b) {
    SDL_SetRenderDrawColor(renderer, r, g, b, SDL_ALPHA_OPAQUE);
    for (const Vector& point: path) {
        SDL_DrawCircle(renderer, point.x, point.y, radius);
    }
    for (size_t i = 1; i < path.size(); i++) {
        SDL_RenderDrawLine(renderer, path[i - 1].x, path[i - 1].y, path[i].x,
            path[i].y);
    }
}

void WorldView::run_kinematics(double dtime) {
    // everything but the endpoints are mobile
    // apply spring force on them + apply obstacle repulsion

    constexpr double k = 0.05;
    constexpr double k2 = 500;
    constexpr double k3 = 5;

    std::fill(local_acc.begin(), local_acc.end(), Vector(0, 0));

    // pass 1: apply spring force
    for (size_t i = 0; i < local_pos.size(); i++) {
        if (i > 0) {
            // add force to previous
            Vector d1 = local_pos[i] - local_pos[i - 1];
            double f1 = -k * (d1.length() - initial_lengths[i - 1]);
            d1.normalize();
            local_acc[i] += f1 * d1;
            local_acc[i - 1] += -f1 * d1;
        }
        if (i < local_pos.size() - 1) {
            // add force to next
            Vector d2 = local_pos[i] - local_pos[i + 1];
            double f2 = -k * (d2.length() + initial_lengths[i]);  // d2 - (-l)
            d2.normalize();
            local_acc[i] += f2 * d2;
            local_acc[i + 1] += -f2 * d2;
        }
    }

    // pass 2: apply repulsive force
    for (size_t i = 1; i < local_pos.size() - 1; i++) {
        for (const Circle& obstacle: obstacles) {
            Vector rvec = local_pos[i] - obstacle.center;
            double r = std::min(rvec.length(), 10.0);
            if (r < obstacle.radius) {
                r = 10;
            } else {
                r -= obstacle.radius;
            }
            rvec.normalize();
            rvec *= (k2 / (r * r));
            local_acc[i] += rvec;
        }
    }

    // pass 3: apply old line force
    for (size_t i = 1; i < local_pos.size() - 1; i++) {
        Vector return_force = old_local_pos[i] - local_pos[i];
        double r = return_force.length();
        return_force.normalize();
        return_force *= k3 * r;
        local_acc[i] += return_force;
    }

    for (size_t i = 1; i < local_pos.size() - 1; i++) {
        local_vel[i] += local_acc[i] * dtime;
        local_pos[i] += local_vel[i] * dtime;
        if (local_vel[i].length() > 100) {
            Log << "error: springs got too fast\n";
            std::exit(1);
        }
    }
}

void WorldView::interpolate_points() {
    assert(global.size() >= 2);
    constexpr size_t STEP_LENGTH = 30;

    local_pos.clear();
    local_vel.clear();
    local_acc.clear();
    initial_lengths.clear();

    Vector start = global[0];
    Vector end = global[1];

    Vector dir = end - start;

    size_t length = (size_t)dir.length();
    dir.normalize();
    dir *= STEP_LENGTH;
    Vector sample = start;
    for (size_t i = 0; i < length; i += STEP_LENGTH) {
        local_pos.push_back(sample);
        sample += dir;
    }

    local_pos.push_back(end);

    old_local_pos = local_pos;

    for (size_t i = 0; i < local_pos.size(); i++) {
        local_vel.push_back(Vector(0, 0));
        local_acc.push_back(Vector(0, 0));
    }
    for (size_t i = 0; i < local_pos.size() - 1; i++) {
        initial_lengths.push_back(local_pos[i].dist(local_pos[i + 1]));
    }
    Path perturbs(local_pos.size(), Vector(0, 0));
    // add perturbation
    for (size_t i = 1; i < local_pos.size() - 1; i++) {
#define rand_double() ((double)(random() % 1000) / 1000.0)
        Vector tangent = local_pos[i + 1] - local_pos[i - 1];
        Vector normal(tangent.y, -tangent.x);
        normal.normalize();
        normal *= (10.0 * rand_double());
        perturbs[i] = normal;
    }
    for (size_t i = 1; i < local_pos.size() - 1; i++) {
        local_pos[i] += perturbs[i];
    }
}

void WorldView::on_event(const SDL_Event& event) {
    keyboard.update(event);
}

void WorldView::draw(SDL_Renderer* renderer, const SDL_Rect* frame,
    double dtime) {
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
    SDL_RenderClear(renderer);
    for (const Circle& obstacle: obstacles) {
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, SDL_ALPHA_OPAQUE);
        SDL_DrawCircle(renderer, obstacle.center.x, obstacle.center.y,
            obstacle.radius);
    }
    draw_path(renderer, global, 10, 64, 128, 255);
    draw_path(renderer, local_pos, 5, 128, 255, 64);
    run_kinematics(dtime);
}
