"""
Appointment Slot Management Module

This module handles the management of available appointment slots for healthcare
providers. It provides functionality to retrieve available slots and book
appointments while maintaining data integrity across multiple healthcare providers.

The module uses a dictionary structure to organize slots by healthcare provider,
allowing for scalable multi-provider support.

Author: Healthcare Chatbot Team
Version: 1.0.0
"""

# Dictionary to store available appointment slots organized by healthcare provider
# Format: {"provider_id": ["YYYY-MM-DD HH:MM", ...]}
available_slots = {
    "doctor1": [
        "2025-06-27 10:00",
        "2025-06-27 11:00",
        "2025-06-27 11:30",
        "2025-06-27 14:00",
    ]
}

def get_available_slots():
    """
    Retrieve all available appointment slots from all healthcare providers.
    
    This function aggregates all available slots from all providers into a single
    flat list, making it easy for the chatbot to present options to users without
    needing to specify a particular provider.
    
    Returns:
        list: A list of available appointment slots in "YYYY-MM-DD HH:MM" format
              from all healthcare providers
        
    Example:
        >>> get_available_slots()
        ['2025-06-27 10:00', '2025-06-27 11:00', '2025-06-27 14:00', '2025-06-28 10:30']
    """
    # Return a flat list of all available slots from all doctors
    all_slots = []
    for doctor_slots in available_slots.values():
        all_slots.extend(doctor_slots)
    return all_slots

def book_slot(slot: str) -> bool:
    """
    Book an appointment slot if it's available.
    
    This function searches through all healthcare providers' schedules to find
    the requested slot and removes it from availability if found. The function
    ensures that only available slots can be booked and prevents double-booking.
    
    Args:
        slot (str): The appointment slot to book in "YYYY-MM-DD HH:MM" format
        
    Returns:
        bool: True if the slot was successfully booked, False if the slot
              was not available or not found
        
    Example:
        >>> book_slot("2025-06-27 10:00")
        True
        >>> book_slot("2025-06-27 10:00")  # Already booked
        False
        >>> book_slot("2025-06-30 15:00")  # Not available
        False
    """
    # Find and remove the slot from any doctor's schedule
    for doctor, slots in available_slots.items():
        if slot in slots:
            slots.remove(slot)
            return True
    return False
