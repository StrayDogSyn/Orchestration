"""
Lab 01: Job Tracker - Original (Buggy) Version

This is the AI-generated code that students will analyze and optimize.

Time Complexity Issues:
- find_by_company(): O(n) - scans entire list
- update_status(): O(n) - scans entire list

Optimal Solution: Use dictionary keyed by company name for O(1) lookup
"""

from typing import List, Dict, Optional


class JobTracker:
    """Track job applications - AI-generated version with performance issues"""
    
    def __init__(self):
        self.applications = []  # List of dicts - this is the bottleneck!
    
    def add_application(self, company: str, position: str, date: str) -> None:
        """
        Add a new job application
        
        Args:
            company: Company name (e.g., "Google")
            position: Job title (e.g., "Software Engineer")
            date: Application date (e.g., "2025-01-15")
        """
        self.applications.append({
            'company': company,
            'position': position,
            'date': date,
            'status': 'pending'
        })
    
    def find_by_company(self, company: str) -> List[Dict]:
        """
        Find all applications to a specific company
        
        ⚠️ PERFORMANCE ISSUE: O(n) complexity
        This method scans the ENTIRE list every time.
        With 1000 applications, that's 1000 comparisons.
        
        Args:
            company: Company name to search for
            
        Returns:
            List of matching applications
        """
        results = []
        for app in self.applications:  # O(n) loop
            if app['company'] == company:
                results.append(app)
        return results
    
    def update_status(self, company: str, position: str, new_status: str) -> bool:
        """
        Update the status of a specific application
        
        ⚠️ PERFORMANCE ISSUE: O(n) complexity
        Also scans the entire list to find a match.
        
        Args:
            company: Company name
            position: Position title
            new_status: New status (e.g., "interview", "rejected", "accepted")
            
        Returns:
            True if found and updated, False otherwise
        """
        for app in self.applications:  # O(n) loop
            if app['company'] == company and app['position'] == position:
                app['status'] = new_status
                return True
        return False
    
    def get_all_applications(self) -> List[Dict]:
        """Get all applications"""
        return self.applications
    
    def count_applications(self) -> int:
        """Get total number of applications"""
        return len(self.applications)


# Example usage (for testing)
if __name__ == "__main__":
    import time
    
    print("=" * 60)
    print("Job Tracker - Performance Test")
    print("=" * 60)
    
    tracker = JobTracker()
    
    # Add 1000 test applications
    print("\n📝 Adding 1000 applications...")
    start = time.time()
    
    for i in range(1000):
        company = f"Company_{i % 100}"  # 100 unique companies
        position = f"Position_{i % 50}"  # 50 unique positions
        tracker.add_application(company, position, "2025-01-01")
    
    end = time.time()
    print(f"   ✅ Added in {end - start:.4f} seconds")
    
    # Test find_by_company performance
    print("\n🔍 Testing find_by_company('Company_42')...")
    start = time.time()
    results = tracker.find_by_company("Company_42")
    end = time.time()
    
    print(f"   ✅ Found {len(results)} applications")
    print(f"   ⏱️  Took {(end - start) * 1000:.4f} milliseconds")
    print(f"   ⚠️  This is O(n) - it checks all {tracker.count_applications()} items!")
    
    # Show what an O(1) lookup would look like
    print("\n💡 With a dictionary (hash map), this would be O(1):")
    print("   ⏱️  Near-instant, regardless of dataset size")
    print("   📈 1000 items? Same speed. 1,000,000 items? Same speed.")
    
    print("\n" + "=" * 60)
