Upgrade-Safe Rules (memorise these)

✅ Extend models
✅ Add new menus
✅ Add reports
✅ Add server actions

❌ Modify core JS
❌ Edit base XML
❌ Change existing fields
❌ Touch enterprise paths


find and read the files
=> find . -type f -exec sh -c 'echo "File: {}"; cat "{}"' \
openning odoo shell
=> ./odoo-bin shell -c odoo.config

reading log file odoo
=> tail -n 100 odoo.log

initialization of oddoo
./odoo-bin -c odoo.conf -i base -d subserve

./odoo-bin -c odoo.conf -u subserve_compliance -d subserve

