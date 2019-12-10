# Local

We use local plugins to customize the look and feel of the University of Denver ArchivesSpace staff interface, and to provide validations for data properties above and beyond what ArchivesSpace provides by default.

In each section of the code, changes made by the plugins are commented with descriptions of what each change sets out to do.

## Backend customizations

The backend customizations override the default MARC export for Resources, to make local customizations to leader and control fields; to provide 33X data fields for RDA content, media, and carrier types; and to include data properties of import to the local catalog, such as OCLC numbers in the 035 data field, and links to [the Archives @ DU Catalog](https://duarchives.coalliance.org) and to [our digital repository](https://specialcollections.du.edu) where appropriate.

## Frontend customizations

* Labels for user-defined and other fields used locally, such as Kaltura IDs for digital object components
* Staff interface look and feel customizations, such as the DU logo
* Changes to the toolbar for integration with other plugins
* Extending the resource tree in order to display archival object component IDs in the third column, for ease of navigation when processing

## Schema extensions

* **archival_object_ext.rb** makes the component ID required at the Archival Object level
* **digital_object_component_ext.rb** validates the optional Component ID field against the Kaltura Entry ID specifications: `/[0-9]_[0-9a-z]{8}/`
* **resource_ext.rb** validates the call number against DU collection identifier guidelines: `/[BDMPTU]\d{3}/`

## Related work

Customizations to the [Archives @ DU Catalog](https://duarchives.coalliance.org), our implementation of the ArchivesSpace public user interface, are found [here](https://github.com/duspeccoll/denver_pui).
