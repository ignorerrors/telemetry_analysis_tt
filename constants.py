# Распределение параметров по категориям
paremeter_categories = {
    "Положение и ориентация": [
        "roll", "pitch", "heading", 
        "altitudeRelative", "altitudeAMSL", "altitudeAboveTerr",
        "estimatorStatus.goodAttitudeEsimate",
        "localPosition.x", "localPosition.y", "localPosition.z"
    ],
    
    "Угловые скорости": [
        "rollRate", "pitchRate", "yawRate",
        "setpoint.rollRate", "setpoint.pitchRate", "setpoint.yawRate"
    ],
    
    "Скорости и высоты": [
        "groundSpeed", "airSpeed", "airSpeedSetpoint", 
        "climbRate", "altitudeTuning", "altitudeTuningSetpoint",
        "localPosition.vx", "localPosition.vy", "localPosition.vz"
    ],
    
    "Навигация": [
        "xTrackError", "rangeFinderDist", "flightDistance", 
        "flightTime", "distanceToHome", "timeToHome",
        "missionItemIndex", "headingToNextWP", "distanceToNextWP",
        "headingToHome", "distanceToGCS",
        "estimatorStatus.goodHorizVelEstimate",
        "estimatorStatus.goodVertVelEstimate",
        "estimatorStatus.goodHorizPosRelEstimate",
        "estimatorStatus.goodHorizPosAbsEstimate",
        "estimatorStatus.goodVertPosAbsEstimate",
        "estimatorStatus.goodVertPosAGLEstimate",
        "estimatorStatus.goodConstPosModeEstimate",
        "estimatorStatus.goodPredHorizPosRelEstimate",
        "estimatorStatus.goodPredHorizPosAbsEstimate"
    ],
    
    "Батарея": [
        "battery0.id", "battery0.batteryFunction", "battery0.batteryType",
        "battery0.voltage", "battery0.current", "battery0.mahConsumed",
        "battery0.temperature", "battery0.percentRemaining",
        "battery0.timeRemaining", "battery0.timeRemainingStr",
        "battery0.chargeState", "battery0.instantPower",
        "throttlePct"
    ],
    
    "Двигатель (EFI)": [
        "efi.health", "efi.ecuIndex", "efi.rpm", 
        "efi.fuelConsumed", "efi.fuelFlow", "efi.engineLoad",
        "efi.sparkTime", "efi.throttlePos", "efi.baroPress",
        "efi.intakePress", "efi.intakeTemp", "efi.cylinderTemp",
        "efi.ignTime", "efi.exGasTemp", "efi.injTime",
        "efi.throttleOut", "efi.ptComp",
        "escStatus.index", "escStatus.rpm1", "escStatus.rpm2",
        "escStatus.rpm3", "escStatus.rpm4", "escStatus.current1",
        "escStatus.current2", "escStatus.current3", "escStatus.current4",
        "escStatus.voltage1", "escStatus.voltage2", "escStatus.voltage3",
        "escStatus.voltage4"
    ],
    
    "GPS": [
        "gps.lat", "gps.lon", "gps.mgrs", "gps.hdop", "gps.vdop",
        "gps.courseOverGround", "gps.lock", "gps.count",
        "gps2.lat", "gps2.lon", "gps2.mgrs", "gps2.hdop", "gps2.vdop",
        "gps2.courseOverGround", "gps2.lock", "gps2.count",
        "estimatorStatus.gpsGlitch"
    ],
    
    "Локальная позиция": [
        "localPositionSetpoint.x", "localPositionSetpoint.y", 
        "localPositionSetpoint.z", "localPositionSetpoint.vx",
        "localPositionSetpoint.vy", "localPositionSetpoint.vz",
        "setpoint.roll", "setpoint.pitch", "setpoint.yaw"
    ],
    
    "Ветер": [
        "wind.direction", "wind.speed", "wind.verticalSpeed"
    ],
    
    "Вибрация": [
        "vibration.xAxis", "vibration.yAxis", "vibration.zAxis",
        "vibration.clipCount1", "vibration.clipCount2", "vibration.clipCount3",
        "estimatorStatus.accelError"
    ],
    
    "Температура": [
        "imuTemp", "battery0.temperature", "efi.intakeTemp",
        "efi.cylinderTemp", "efi.exGasTemp",
        "temperature.temperature1", "temperature.temperature2", 
        "temperature.temperature3",
        "hygrometer.temperature", "generator.rectifierTemp", 
        "generator.genTemp"
    ],
    
    "Влажность": [
        "hygrometer.humidity", "hygrometer.hygrometerid"
    ],
    
    "Генератор": [
        "generator.status", "generator.genSpeed", "generator.batteryCurrent",
        "generator.loadCurrent", "generator.powerGenerated", "generator.busVoltage",
        "generator.batCurrentSetpoint", "generator.rectifierTemp", "generator.genTemp",
        "generator.runtime", "generator.timeMaintenance"
    ],
    
    "Датчики расстояния": [
        "distanceSensor.rotationNone", "distanceSensor.rotationYaw45",
        "distanceSensor.rotationYaw90", "distanceSensor.rotationYaw135",
        "distanceSensor.rotationYaw180", "distanceSensor.rotationYaw225",
        "distanceSensor.rotationYaw270", "distanceSensor.rotationYaw315",
        "distanceSensor.rotationPitch90", "distanceSensor.rotationPitch270",
        "distanceSensor.minDistance", "distanceSensor.maxDistance"
    ],
    
    "Террейн": [
        "terrain.blocksPending", "terrain.blocksLoaded"
    ],
    
    "Статус и мониторинг": [
        "estimatorStatus.velRatio", "estimatorStatus.horizPosRatio",
        "estimatorStatus.vertPosRatio", "estimatorStatus.magRatio",
        "estimatorStatus.haglRatio", "estimatorStatus.tasRatio",
        "estimatorStatus.horizPosAccuracy", "estimatorStatus.vertPosAccuracy"
    ],
    
    "Время и системные параметры": [
        "Timestamp", "hobbs", "clock.currentTime", 
        "clock.currentUTCTime", "clock.currentDate"
    ]
}

"""Градусы (°), Градусы в секунду (°/с), Градусы Цельсия (°C)
Метры в секунду (м/с), Метры (м)
Вольты (В), Амперы (А), Ватты (Вт)
Обороты в минуту (об/мин), Миллиампер-часы (мА·ч)
Часы (ч), Секунды (с), Минуты (мин)
Литры в час (л/ч), Литр (л), Проценты (%)
Миллисекунды (мс), G-силы (g), Килопаскали (кПа)"""

# Единицы измерения для параметров
parameter_units = {
    "Timestamp": "",
    "roll": "°",
    "pitch": "°",
    "heading": "°",
    "rollRate": "°/с",
    "pitchRate": "°/с",
    "yawRate": "°/с",
    "groundSpeed": "м/с",
    "airSpeed": "м/с",
    "airSpeedSetpoint": "м/с",
    "climbRate": "м/с",
    "altitudeRelative": "м",
    "altitudeAMSL": "м",
    "altitudeAboveTerr": "м",
    "altitudeTuning": "м",
    "altitudeTuningSetpoint": "м",
    "xTrackError": "м",
    "rangeFinderDist": "м",
    "flightDistance": "м",
    "flightTime": "с",
    "distanceToHome": "м",
    "timeToHome": "с",
    "missionItemIndex": "",
    "headingToNextWP": "°",
    "distanceToNextWP": "м",
    "headingToHome": "°",
    "distanceToGCS": "м",
    "throttlePct": "%",
    "imuTemp": "°C",
    "hobbs": "ч",
    "battery0.id": "",
    "battery0.batteryFunction": "",
    "battery0.batteryType": "",
    "battery0.voltage": "В",
    "battery0.current": "А",
    "battery0.mahConsumed": "мА·ч",
    "battery0.temperature": "°C",
    "battery0.percentRemaining": "%",
    "battery0.timeRemaining": "мин",
    "battery0.timeRemainingStr": "",
    "battery0.chargeState": "",
    "battery0.instantPower": "Вт",
    "clock.currentTime": "",
    "clock.currentUTCTime": "",
    "clock.currentDate": "",
    "distanceSensor.rotationNone": "м",
    "distanceSensor.rotationYaw45": "м",
    "distanceSensor.rotationYaw90": "м",
    "distanceSensor.rotationYaw135": "м",
    "distanceSensor.rotationYaw180": "м",
    "distanceSensor.rotationYaw225": "м",
    "distanceSensor.rotationYaw270": "м",
    "distanceSensor.rotationYaw315": "м",
    "distanceSensor.rotationPitch90": "м",
    "distanceSensor.rotationPitch270": "м",
    "distanceSensor.minDistance": "м",
    "distanceSensor.maxDistance": "м",
    "efi.health": "",
    "efi.ecuIndex": "",
    "efi.rpm": "об/мин",
    "efi.fuelConsumed": "л",
    "efi.fuelFlow": "л/ч",
    "efi.engineLoad": "%",
    "efi.sparkTime": "мс",
    "efi.throttlePos": "%",
    "efi.baroPress": "кПа",
    "efi.intakePress": "кПа",
    "efi.intakeTemp": "°C",
    "efi.cylinderTemp": "°C",
    "efi.ignTime": "мс",
    "efi.exGasTemp": "°C",
    "efi.injTime": "мс",
    "efi.throttleOut": "%",
    "efi.ptComp": "",
    "escStatus.index": "",
    "escStatus.rpm1": "об/мин",
    "escStatus.rpm2": "об/мин",
    "escStatus.rpm3": "об/мин",
    "escStatus.rpm4": "об/мин",
    "escStatus.current1": "А",
    "escStatus.current2": "А",
    "escStatus.current3": "А",
    "escStatus.current4": "А",
    "escStatus.voltage1": "В",
    "escStatus.voltage2": "В",
    "escStatus.voltage3": "В",
    "escStatus.voltage4": "В",
    "estimatorStatus.goodAttitudeEsimate": "",
    "estimatorStatus.goodHorizVelEstimate": "",
    "estimatorStatus.goodVertVelEstimate": "",
    "estimatorStatus.goodHorizPosRelEstimate": "",
    "estimatorStatus.goodHorizPosAbsEstimate": "",
    "estimatorStatus.goodVertPosAbsEstimate": "",
    "estimatorStatus.goodVertPosAGLEstimate": "",
    "estimatorStatus.goodConstPosModeEstimate": "",
    "estimatorStatus.goodPredHorizPosRelEstimate": "",
    "estimatorStatus.goodPredHorizPosAbsEstimate": "",
    "estimatorStatus.gpsGlitch": "",
    "estimatorStatus.accelError": "",
    "estimatorStatus.velRatio": "",
    "estimatorStatus.horizPosRatio": "",
    "estimatorStatus.vertPosRatio": "",
    "estimatorStatus.magRatio": "",
    "estimatorStatus.haglRatio": "",
    "estimatorStatus.tasRatio": "",
    "estimatorStatus.horizPosAccuracy": "м",
    "estimatorStatus.vertPosAccuracy": "м",
    "generator.status": "",
    "generator.genSpeed": "об/мин",
    "generator.batteryCurrent": "А",
    "generator.loadCurrent": "А",
    "generator.powerGenerated": "Вт",
    "generator.busVoltage": "В",
    "generator.batCurrentSetpoint": "А",
    "generator.rectifierTemp": "°C",
    "generator.genTemp": "°C",
    "generator.runtime": "ч",
    "generator.timeMaintenance": "ч",
    "gps.lat": "°",
    "gps.lon": "°",
    "gps.mgrs": "",
    "gps.hdop": "",
    "gps.vdop": "",
    "gps.courseOverGround": "°",
    "gps.lock": "",
    "gps.count": "",
    "gps2.lat": "°",
    "gps2.lon": "°",
    "gps2.mgrs": "",
    "gps2.hdop": "",
    "gps2.vdop": "",
    "gps2.courseOverGround": "°",
    "gps2.lock": "",
    "gps2.count": "",
    "hygrometer.temperature": "°C",
    "hygrometer.humidity": "%",
    "hygrometer.hygrometerid": "",
    "localPosition.x": "м",
    "localPosition.y": "м",
    "localPosition.z": "м",
    "localPosition.vx": "м/с",
    "localPosition.vy": "м/с",
    "localPosition.vz": "м/с",
    "localPositionSetpoint.x": "м",
    "localPositionSetpoint.y": "м",
    "localPositionSetpoint.z": "м",
    "localPositionSetpoint.vx": "м/с",
    "localPositionSetpoint.vy": "м/с",
    "localPositionSetpoint.vz": "м/с",
    "setpoint.roll": "°",
    "setpoint.pitch": "°",
    "setpoint.yaw": "°",
    "setpoint.rollRate": "°/с",
    "setpoint.pitchRate": "°/с",
    "setpoint.yawRate": "°/с",
    "temperature.temperature1": "°C",
    "temperature.temperature2": "°C",
    "temperature.temperature3": "°C",
    "terrain.blocksPending": "",
    "terrain.blocksLoaded": "",
    "vibration.xAxis": "g",
    "vibration.yAxis": "g",
    "vibration.zAxis": "g",
    "vibration.clipCount1": "",
    "vibration.clipCount2": "",
    "vibration.clipCount3": "",
    "wind.direction": "°",
    "wind.speed": "м/с",
    "wind.verticalSpeed": "м/с"
}