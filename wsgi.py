import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

try:
    logger.debug("Starting to import create_app")
    from app.app import create_app
    logger.debug("Successfully imported create_app")
    
    logger.debug("Creating Flask application")
    app = create_app()
    logger.debug("Flask application created successfully")
    
except Exception as e:
    logger.error(f"Failed to create application: {str(e)}", exc_info=True)
    raise

if __name__ == "__main__":
    logger.debug("Starting Flask application")
    app.run(host='0.0.0.0', port=5000)