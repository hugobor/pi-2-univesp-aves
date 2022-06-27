from storages.backends.azure_storage import AzureStorage

from django.conf import settings

#https://davidsantiago.fr/django-using-azure-blob-storage-to-handle-static-media-assets-from-scratch/

class AzureMediaStorage( AzureStorage ):
    """Configuração de armazenamento de mídia no Azure."""
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_ACCOUNT_KEY
    azure_container = 'media'
    expiration_secs = None

    
class AzureStaticStorage( AzureStorage ):
    """Configuração de armazenamento de arquivos estáticos no Azure."""
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_ACCOUNT_KEY    
    azure_container = 'static'
    expiration_secs = None    
