/*
This code is taken verbatim from
https://stackoverflow.com/questions/38334081/how-to-draw-circles-arcs-and-vector-graphics-in-sdl
I do not claim copyright or ownership.
I have made certain modifications
*/

#include "midpoint.h"

void SDL_DrawCircle_Outline(SDL_Renderer* renderer, int32_t centreX,
    int32_t centreY, int32_t radius) {
    if (centreX + radius < 0 || centreY + radius < 0) {
        return;
    }
    if (centreX - radius > 700 || centreY - radius > 700) {
        return;
    }

    const int32_t diameter = (radius * 2);

    int32_t x = (radius - 1);
    int32_t y = 0;
    int32_t tx = 1;
    int32_t ty = 1;
    int32_t error = (tx - diameter);

    while (x >= y) {
        //  Each of the following renders an octant of the circle
        SDL_RenderDrawPoint(renderer, centreX + x, centreY - y);
        SDL_RenderDrawPoint(renderer, centreX + x, centreY + y);
        SDL_RenderDrawPoint(renderer, centreX - x, centreY - y);
        SDL_RenderDrawPoint(renderer, centreX - x, centreY + y);
        SDL_RenderDrawPoint(renderer, centreX + y, centreY - x);
        SDL_RenderDrawPoint(renderer, centreX + y, centreY + x);
        SDL_RenderDrawPoint(renderer, centreX - y, centreY - x);
        SDL_RenderDrawPoint(renderer, centreX - y, centreY + x);

        if (error <= 0) {
            ++y;
            error += ty;
            ty += 2;
        }

        if (error > 0) {
            --x;
            tx += 2;
            error += (tx - diameter);
        }
    }
}

void SDL_DrawCircle(SDL_Renderer* renderer, int32_t center_x, int32_t center_y,
    int32_t radius) {
    for (int32_t r = 1; r < radius; r++) {
        SDL_DrawCircle_Outline(renderer, center_x, center_y, r);
    }
}
