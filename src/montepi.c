// A faster version of montepi.py
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <math.h>

// Use a custom LFSR for PRNG

// Implement 32 bit XORShift
struct xor32 {
    uint32_t state;
};

uint32_t shiftxor32(struct xor32* __restrict gen) {
    uint32_t x = gen->state;
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;

    gen->state = x;

    return x;
}

float montepi(struct xor32* __restrict gen, int N) {
    int inside = 0;

    float x, y, dist;
    for (int i = 0; i < N; ++i) {
        // get random point 
        x = ((float)shiftxor32(gen)/((float)UINT32_MAX))*2 + -1;
        y = ((float)shiftxor32(gen)/((float)UINT32_MAX))*2 + -1;
        // get distance from origin
        dist = x*x + y*y;
        // add to accumulator
        inside += dist < 1;
    }

    return 4.0 * (inside / (float)N);
}

int main(void) {
    struct xor32 gen;
    gen.state = time(NULL);

    int points = 100000000;
    float pi = montepi(&gen, points);

    printf("pi is approx: %f\n", pi);
}