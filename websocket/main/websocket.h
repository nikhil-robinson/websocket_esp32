#if !defined(WEBSOCKET_H_)
#define WEBSOCKET_H_

#include <stdio.h>
#include <string.h>
#include <sys/param.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_system.h"
#include "esp_websocket_client.h"

void start_websocket(void);

#endif // WEBSOCKET_H_
