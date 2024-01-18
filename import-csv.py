import csv

def convert_to_csv(input_text, output_file):
    # Split the input text into lines
    lines = input_text.strip().split('\n')

    # Prepare to write to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Process each line
        for line in lines:
            # Split line into parts based on multiple spaces
            parts = line.split('  ')
            # Filter out empty strings and strip each part
            parts = [part.strip() for part in parts if part.strip()]
            # Write to CSV
            csvwriter.writerow(parts)

# Input text data (replace this with your actual data)
input_text = """
   Package       Name                                               Status    Version  
 ------------- -------------------------------------------------- --------- --------- 
  Core          Announcements (announcements_feed)                 Enabled   10.2.1   
  Core          Automated Cron (automated_cron)                    Enabled   10.2.1   
  Core          BigPipe (big_pipe)                                 Enabled   10.2.1   
  Core          Block (block)                                      Enabled   10.2.1   
  Core          Block Content (block_content)                      Enabled   10.2.1   
  Core          Breakpoint (breakpoint)                            Enabled   10.2.1   
  Core          CKEditor 5 (ckeditor5)                             Enabled   10.2.1   
  Core          Comment (comment)                                  Enabled   10.2.1   
  Core          Configuration Manager (config)                     Enabled   10.2.1   
  Core          Contact (contact)                                  Enabled   10.2.1   
  Core          Contextual Links (contextual)                      Enabled   10.2.1   
  Field types   Datetime (datetime)                                Enabled   10.2.1   
  Core          Database Logging (dblog)                           Enabled   10.2.1   
  Core          Internal Dynamic Page Cache (dynamic_page_cache)   Enabled   10.2.1   
  Core          Text Editor (editor)                               Enabled   10.2.1   
  Core          Field (field)                                      Enabled   10.2.1   
  Core          Field UI (field_ui)                                Enabled   10.2.1   
  Field types   File (file)                                        Enabled   10.2.1   
  Core          Filter (filter)                                    Enabled   10.2.1   
  Core          Help (help)                                        Enabled   10.2.1   
  Core          History (history)                                  Enabled   10.2.1   
  Field types   Image (image)                                      Enabled   10.2.1   
  Field types   Link (link)                                        Enabled   10.2.1   
  Core          Custom Menu Links (menu_link_content)              Enabled   10.2.1   
  Core          Menu UI (menu_ui)                                  Enabled   10.2.1   
  Migration     Migrate (migrate)                                  Enabled   10.2.1   
  Core          MySQL (mysql)                                      Enabled   10.2.1   
  Core          Node (node)                                        Enabled   10.2.1   
  Field types   Options (options)                                  Enabled   10.2.1   
  Core          Internal Page Cache (page_cache)                   Enabled   10.2.1   
  Core          Path (path)                                        Enabled   10.2.1   
  Core          Path alias (path_alias)                            Enabled   10.2.1   
  Core          Search (search)                                    Enabled   10.2.1   
  Core          Shortcut (shortcut)                                Enabled   10.2.1   
  Core          System (system)                                    Enabled   10.2.1   
  Core          Taxonomy (taxonomy)                                Enabled   10.2.1   
  Field types   Text (text)                                        Enabled   10.2.1   
  Core          Toolbar (toolbar)                                  Enabled   10.2.1   
  Core          Update Manager (update)                            Enabled   10.2.1   
  Core          User (user)                                        Enabled   10.2.1   
  Core          Views (views)                                      Enabled   10.2.1   
  Core          Views UI (views_ui)                                Enabled   10.2.1   
  Migration     Migrate Plus (migrate_plus)                        Enabled   6.0.2    
  Migration     Migrate Tools (migrate_tools)                      Enabled   6.0.2            
"""

# Output CSV file name
output_file = 'output-D10.csv'

# Convert and save to CSV
convert_to_csv(input_text, output_file)
print(f"Data converted to CSV and saved as {output_file}")
