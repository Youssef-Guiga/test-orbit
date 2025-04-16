import os
import uuid

def main():
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("Error: API_KEY is missing!")
        exit(1)
    
    print(f"✅ Build started with API_KEY: {api_key[:4]}***")
    
    build_id = uuid.uuid4()
    print(f"📦 Build ID: {build_id}")
    print("🚀 Hello from the build process!")

if __name__ == "__main__":
    main()
