/*
 * HARINETRA BMS Firmware
 * (c) 2025 Swdeshi
 */

#include "bms.h"
int main(void) {
    BMS_Init();
    while (1) {
        BMS_Update();
    }
    return 0;
}
