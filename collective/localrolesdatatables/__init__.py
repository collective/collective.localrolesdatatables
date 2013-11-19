from Products.CMFCore.CMFCatalogAware import CatalogAware

CatalogAware._cmf_security_indexes += ('hasLocalRoles',)
