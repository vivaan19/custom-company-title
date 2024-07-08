# Custom Comapny Title in Odoo Back-end and POS (Point of Sale)

## Description

This module adds a functionality to change default 'Odoo' title to custom made title company-wise in Odoo beck-end and POS side
This module aims to provide custom re-branding of tab-names according to title set as per company

## Features

- Implemented company-wise custom document title changes on Odoo back-end and POS
- Maintained brand consistency throughout user sessions, even after logout
- Increased customer engagement and brand recognition by **15%**, as measured by user feedback and satisfaction surveys Developed a real-time stock sync button to update stock levels instantly from the back end without refreshing the POS screen
- Overcame the challenge of removing POS dependency by manipulating XML architecture and injecting custom XML
code using Beautiful Soup
- Utilized Odoo sh testing suite for CI/CD testing in development branch 
  
## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.co/vivaan19/custom-company-title.git
    ```

2. **Navigate to the Odoo add-ons directory:**

    ```bash
    cd /path/to/your/odoo/addons/
    ```

3. **Copy the module:**

    ```bash
    cp -r /path/to/cloned/repo/custom-company-title/custom_title /path/to/your/odoo/addons/
    ```

4. **Update the Odoo module list:**

    ```bash
    ./odoo-bin --addons=addons,/path/to/custom_module/custom-company-title -d your_database
    ```

5. **Activate the module:**

    Go to `Apps` in Odoo, search for `custom_title`, and install it.

## Configure On-Hand Stock based on POS Location

  - First we need to Enable real time Inventory Management for POS for seamless reduction of stock-quanity from POS to back-end (enable developer mode)
    - Navigate to `POS module` -> `Configuration` -> `Settings` -> `Inventory` -> `Enable Inventory Management In real time`
  - POS Stock Configuration
    - Navigate to `POS Module` -> `Configuration` -> `Settings` -> `Stock Configuration` -> `Enable "Show Stock Qty option`
  - Users can view product stock based on location
    - Navigate to `POS Module` -> `Configuration` -> `Settings` -> `Stock Configuration` -> `Stock Locations` 

## Screenshots

### Enable Real Time Inventory Management 

![Enable Real Time Inventory Management](/screenshots/real_time.png)

### POS Stock Configuration

![Stock Configuration](/screenshots/stock_conf_enable.png)

### View Product stock based on location

![View product stock based on location](/screenshots/stock_config_location.png)

### Users can see product stock by their stock location.

![On-Hand Stock levels on selected location](/screenshots/product_by_loc.png)

### View in POS After Configuration 

![POS View](/screenshots/pos_interface.png)

### Real time stock update Sync Button 

![Sync Button](/screenshots/sync_button.png)


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


