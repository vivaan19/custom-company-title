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

## Configure Custom Title in POS and Odoo ERP Back-end

  - First we need to custom document title which is below Favicon inside company
    - Navigate to `Setting` -> `User & Companies` -> `Select a company` -> `Document title` -> `Write your custom title`
  - POS Configuration - after installing POS module 
    - Navigate to `POS Module` -> `Configuration` -> `Settings` -> `Custom title in POS` -> `Enable Custom Title in POS`
  
## Screenshots

### Company Configuration 

![Input Custom title in Company](/screenshots/company_config.png)

### Multi-Company Title Install 

![Different title for different companies](/screenshots/multi_company_title.png)

### Title after logout

![Title after logout](/screenshots/title_after_logout.png)

### When POS module is installed custom title can be configured 

![Enable Custom title POS Module](/screenshots/config_pos_install.png)

### POS Interface after Enabling Custom title in POS

![POS View](/screenshots/pos_screen.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


