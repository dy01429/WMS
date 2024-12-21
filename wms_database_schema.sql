
-- 1. Table for Clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_address VARCHAR(255),
    contact_details VARCHAR(255)
);

-- 2. Table for Pallets
CREATE TABLE pallets (
    pallet_id INT AUTO_INCREMENT PRIMARY KEY,
    pallet_label VARCHAR(255) UNIQUE NOT NULL,
    pallet_quality VARCHAR(100) NOT NULL CHECK (pallet_quality IN ('Good', 'Bad', 'Damaged')), 
    capacity DECIMAL(10, 2) NOT NULL CHECK (capacity > 0)  -- Ensure positive capacity
);

-- 3. Table for Boxes
CREATE TABLE boxes (
    box_id INT AUTO_INCREMENT PRIMARY KEY,
    box_label VARCHAR(255) UNIQUE NOT NULL,
    length DECIMAL(10, 2) NOT NULL,  -- Length in meters or other units
    width DECIMAL(10, 2) NOT NULL, 
    height DECIMAL(10, 2) NOT NULL,
    weight DECIMAL(10, 2) NOT NULL CHECK (weight > 0),  -- Ensure positive weight
    pallet_id INT,
    FOREIGN KEY (pallet_id) REFERENCES pallets(pallet_id)
);

-- 4. Table for Inventory
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    box_id INT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (box_id) REFERENCES boxes(box_id)
);

-- 5. Table for Pallet Movements
CREATE TABLE pallet_movements (
    movement_id INT AUTO_INCREMENT PRIMARY KEY,
    pallet_id INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    from_zone VARCHAR(50),
    to_zone VARCHAR(50),
    barcode VARCHAR(255),
    FOREIGN KEY (pallet_id) REFERENCES pallets(pallet_id)
);

-- 6. Table for Box Stacking Configuration
CREATE TABLE box_stacking (
    stack_id INT AUTO_INCREMENT PRIMARY KEY,
    pallet_id INT NOT NULL,
    box_id INT NOT NULL,
    stack_level INT NOT NULL CHECK (stack_level >= 0),  -- Stack levels must be non-negative
    FOREIGN KEY (pallet_id) REFERENCES pallets(pallet_id),
    FOREIGN KEY (box_id) REFERENCES boxes(box_id),
    UNIQUE (pallet_id, box_id)  -- Prevent duplicate entries for the same box on the same pallet
);
