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