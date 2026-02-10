# Disney IT: IoT Device Battery Auditor
# Aimed at: System Administration & Maintenance 

def run_battery_audit():
    # Data: [Device ID, Battery Percentage, Location]
    devices = [
        ["MB-001", 82, "Magic Kingdom Entrance"],
        ["MB-002", 15, "EPCOT Ticketing"],
        ["MB-003", 54, "Hollywood Studios Gate"],
        ["MB-004", 08, "Animal Kingdom Lodge"],
        ["MB-005", 99, "Disney Springs Scanner"]
    ]

    print("--- 🔋 Disney IoT Infrastructure: Battery Health Audit ---")
    
    maintenance_required = []

    for device in devices:
        device_id = device[0]
        battery = device[1]
        location = device[2]

        if battery < 20:
            status = "🚨 CRITICAL"
            maintenance_required.append(f"{device_id} at {location}")
        elif battery < 50:
            status = "⚠️ LOW"
        else:
            status = "✅ HEALTHY"
            
        print(f"Device: {device_id} | Battery: {battery}% | Status: {status}")

    # Final Audit Summary
    print("\n--- 🛠️ Maintenance Ticket Summary ---")
    if maintenance_required:
        print("Tickets created for the following locations:")
        for item in maintenance_required:
            print(f"- {item}")
    else:
        print("All systems within operational battery range.")

run_battery_audit()
