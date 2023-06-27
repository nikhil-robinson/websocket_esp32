#include <stdio.h>
#include "esp_wifi.h"
#include "freertos/task.h"
#include "esp_event.h"
#include "freertos/FreeRTOS.h"
#include "wifi.h"
#include "websocket.h"
#include "esp_websocket_client.h"

void app_main(void)
{
    connect_wifi();
    printf("wifi_init");
    start_websocket();
    printf("done");
}
