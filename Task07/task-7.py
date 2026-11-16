"""Task 7: Design a Contact-Merging Program from First Principles."""

def merge_contacts(contacts):
    # Union-find or connected component clustering based on shared phone/email
    parent = list(range(len(contacts)))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i

    phone_map = {}
    email_map = {}
    
    for idx, c in enumerate(contacts):
        for p in c.get("phones", []):
            if p in phone_map:
                union(idx, phone_map[p])
            else:
                phone_map[p] = idx
        for e in c.get("emails", []):
            if e in email_map:
                union(idx, email_map[e])
            else:
                email_map[e] = idx
                
    merged = {}
    for idx in range(len(contacts)):
        root = find(idx)
        if root not in merged:
            merged[root] = {"names": set(), "phones": set(), "emails": set()}
        merged[root]["names"].add(contacts[idx]["name"])
        merged[root]["names"].update(contacts[idx].get("aliases", []))
        merged[root]["phones"].update(contacts[idx].get("phones", []))
        merged[root]["emails"].update(contacts[idx].get("emails", []))
        
    return list(merged.values())

if __name__ == "__main__":
    sample_contacts = [
        {"name": "Sam Agal", "phones": ["9840012345"], "emails": ["sam@gmail.com"]},
        {"name": "S. Agal", "phones": ["9840012345"], "emails": ["sam.work@company.com"]},
        {"name": "Rei", "phones": ["9840099999"], "emails": ["rei@evangelion.net"]}
    ]
    
    result = merge_contacts(sample_contacts)
    print("Merged Contacts Result:")
    for rc in result:
        print(f"Names: {rc['names']} | Phones: {rc['phones']} | Emails: {rc['emails']}")
