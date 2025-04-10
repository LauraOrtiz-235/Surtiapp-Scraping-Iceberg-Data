from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, Query
from scraping import scrape_category as scrape_function

# =================================================================
# FAST API CONFIGURATION
# =================================================================
YOUR_NAME = "Laura Sofia Ortiz" #TODO: UPDATE WITH YOUR NAME

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=f"Surtiapp Scraping API - Developed by {YOUR_NAME}",
        version="1.0.0",    
        description="Technical Assesment Test for the position of Data Solutions & Automation Engineer at Iceberg Data. This API is used to scrape the Surtiapp website and extract product information.", 
        routes=app.routes
    )
    
    if "HTTPValidationError" in openapi_schema["components"]["schemas"]:
        del openapi_schema["components"]["schemas"]["HTTPValidationError"]
    if "ValidationError" in openapi_schema["components"]["schemas"]:
        del openapi_schema["components"]["schemas"]["ValidationError"]
    
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.pop("servers", None)
            if "responses" in method:
                if "422" in method["responses"]:
                    del method["responses"]["422"]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()
app.openapi = custom_openapi


# =================================================================
# API ENDPOINTS
# =================================================================
# Redirect to the documentation
@app.get("/", include_in_schema=False, response_class=RedirectResponse, tags=["Root"])
async def redirect_to_docs():
    return "/docs"

# Scraping function
@app.get("/scrapeCategory", tags=["Scraping"])
async def scrape_category(
            url: str = Query(..., description="The URL of the category page to scrape")
        ) -> list:
    return scrape_function(url)


# =================================================================
# TESTING
# =================================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)