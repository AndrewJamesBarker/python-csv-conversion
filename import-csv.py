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
  Core           Announcements (announcements_feed)                 Enabled   10.2.2   
  Core           Automated Cron (automated_cron)                    Enabled   10.2.2   
  Core           BigPipe (big_pipe)                                 Enabled   10.2.2   
  Core           Block (block)                                      Enabled   10.2.2   
  Core           Block Content (block_content)                      Enabled   10.2.2   
  Core           Breakpoint (breakpoint)                            Enabled   10.2.2   
  Core           CKEditor 5 (ckeditor5)                             Enabled   10.2.2   
  Core           Comment (comment)                                  Enabled   10.2.2   
  Core           Configuration Manager (config)                     Enabled   10.2.2   
  Multilingual   Content Translation (content_translation)          Enabled   10.2.2   
  Core           Contextual Links (contextual)                      Enabled   10.2.2   
  Field types    Datetime (datetime)                                Enabled   10.2.2   
  Core           Database Logging (dblog)                           Enabled   10.2.2   
  Core           Internal Dynamic Page Cache (dynamic_page_cache)   Enabled   10.2.2   
  Core           Text Editor (editor)                               Enabled   10.2.2   
  Core           Field (field)                                      Enabled   10.2.2   
  Core           Field UI (field_ui)                                Enabled   10.2.2   
  Field types    File (file)                                        Enabled   10.2.2   
  Core           Filter (filter)                                    Enabled   10.2.2   
  Core           Help (help)                                        Enabled   10.2.2   
  Core           History (history)                                  Enabled   10.2.2   
  Field types    Image (image)                                      Enabled   10.2.2   
  Multilingual   Language (language)                                Enabled   10.2.2   
  Field types    Link (link)                                        Enabled   10.2.2   
  Multilingual   Interface Translation (locale)                     Enabled   10.2.2   
  Core           Custom Menu Links (menu_link_content)              Enabled   10.2.2   
  Core           Menu UI (menu_ui)                                  Enabled   10.2.2   
  Migration      Migrate (migrate)                                  Enabled   10.2.2   
  Migration      Migrate Drupal (migrate_drupal)                    Enabled   10.2.2   
  Migration      Migrate Drupal UI (migrate_drupal_ui)              Enabled   10.2.2   
  Core           MySQL (mysql)                                      Enabled   10.2.2   
  Core           Node (node)                                        Enabled   10.2.2   
  Field types    Options (options)                                  Enabled   10.2.2   
  Core           Internal Page Cache (page_cache)                   Enabled   10.2.2   
  Core           Path (path)                                        Enabled   10.2.2   
  Core           Path alias (path_alias)                            Enabled   10.2.2   
  Core           Password Compatibility (phpass)                    Enabled   10.2.2   
  Core           Search (search)                                    Enabled   10.2.2   
  Core           Shortcut (shortcut)                                Enabled   10.2.2   
  Core           Statistics (statistics)                            Enabled   10.2.2   
  Core           System (system)                                    Enabled   10.2.2   
  Core           Taxonomy (taxonomy)                                Enabled   10.2.2   
  Field types    Telephone (telephone)                              Enabled   10.2.2   
  Field types    Text (text)                                        Enabled   10.2.2   
  Core           Toolbar (toolbar)                                  Enabled   10.2.2   
  Core           Update Manager (update)                            Enabled   10.2.2   
  Core           User (user)                                        Enabled   10.2.2   
  Core           Views (views)                                      Enabled   10.2.2   
  Core           Views UI (views_ui)                                Enabled   10.2.2   
  Migration      Migrate Plus (migrate_plus)                        Enabled   6.0.2    
  Migration      Migrate Tools (migrate_tools)                      Enabled   6.0.2             
"""

# Output CSV file name
output_file = 'output-D10.csv'

# Convert and save to CSV
convert_to_csv(input_text, output_file)
print(f"Data converted to CSV and saved as {output_file}")
