# Expedition Marine UDP Bidirectional Control Reference

This is a technical guide to the canonical UDP message interface used for remote control and status with Expedition Marine. These commands are utilized for bidirectional (send and receive) race management and navigation actions such as pin set, mark control, course selection, and sail recommendations.

---

## Command Reference Table

| Command / Message         | Syntax / Example                                             | Direction   |Description                                                              |
|-----------------------    |------------------------------------------------------------- |:----------- |-------------------------------------------------------------------------|
| **Set Handsake**          | `#S,GETUSERCHANNELNAMES*0C\r\n`                              | App → EM    | Send authentication handshake once at startup.                          |
| **Set Port Pin**          | `#L,P*13\r\n`                                                | App → EM    | Set port pin location (latitude, longitude).                            |
| **Set Starboard Pin**     | `#L,S*10\r\n`                                                | App → EM    | Set starboard pin location.                                             |
| **Start 15 min Timer**    | `#G,15.00*62\r\n`                                            | App → EM    | Start 15 minute Start Timer.                                            |
| **Start 10 min Timer**    | `#G,10.00*67\r\n`                                            | App → EM    | Start 10 minute Start Timer.                                            |
| **Start  5 min Timer**    | `#G,5.00*53\r\n`                                             | App → EM    | Start 5 minute Start Timer.                                             |
| **Start  3 min Timer**    | `#G,3.00*55\r\n`                                             | App → EM    | Start 3 minute Start Timer.                                             |
| **Sync the Timer**        | `#G,SYNC*4F\r\n`                                             | App → EM    | Sync the Start Timer the nearest whole minute                           |
| **Kill the Timer**        | `#G,-1.00*7A\r\n`                                            | App → EM    | Kill the Start Timer.                                                   |
| **Query Active Mark**     | `#M,QUERY*08\r\n`                                            | App ↔ EM    | Get the current active mark (name, lat, lon).                           |
| **Query All Marks**       | `#M,QUERYALL*49\r\n`                                         | App ↔ EM    | List all marks (name, latitude, longitude).                             |
| **Go to Next Mark**       | `#M,NEXT*45\r\n`                                             | App → EM    | Advance to the next mark in the course.                                 |
| **Go to Previous Mark**.  | `#M,PREV*53\r\n`                                             | App → EM    | Move to the previous mark in the course.                                |
| **Receive Active Mark**.  | `#M,ACTIVE,LYC-A,40.709396,-74.031496,M*18`                  | App → EM    | Receive active mark.                                                    |
| **Get Course Total**      | `#C,GETCOURSENUM*51\r\n`                                     | App → EM    | Get the number of saved courses.                                        |
| **Receive Course Number** | `#C,COURSENUM*51\r\n`                                        | EM → App    | Receive the number of saved courses.                                    |
| **Receive Course Name**.  | `#C,GETCOURSENAME,32,LCR-C8*5C`                              | EM → App    | Receive the course name.                                                |
| **Set Course**            | `#C,SETCOURSE,1*0E\r\n`                                      | App → EM    | Set the selected course with ID 1                                       |
| **Send MOB**              | `#M,MOB*02\r\n`                                              | App → EM    | Start Man Over Board.                                                   |
| **Clear MOB**             | `#M,CLEAR*1A\r\n`                                            | App → EM    | Clear Man Over Board.                                                   |

---

### Direction

- `App → EM` : from your SailWatchPro app to Expedition Marine
- `EM → App` : from Expedition Marine to your app
- `App ↔ EM` : can be used bidirectionally; request & response

---

## General Format Rules

- Commands use comma-separated ASCII text.
- Each message starts with `#` and ends with `*CS\r\n`, where `CS` is a checksum (XOR of all characters between `#` and `*`).
- All parameters are required, except for optional Lat/Long (e.g., in MOB command).
- No duplicated message types for wind, weather, or app-specific sync.

## Swift Checksum Calculator for Expedition Marine

```
  private func calculateCorrectChecksum(_ command: String) -> String {
        // Calculate XOR checksum including the # character (official EM protocol)
        // XOR all characters from start up to (but not including) the '*' character
        if let asteriskIndex = command.firstIndex(of: "*") {
            let dataToCheck = String(command[..<asteriskIndex])
            let checksum = dataToCheck.utf8.reduce(0) { $0 ^ $1 }
            return String(format: "%02X", checksum)
        }
        return "00"
    }
```

---

## Examples

- **Set Port Pin:**<br>
 `#P,PORT,40.123,-73.987*AA\r\n`
- **Next Mark:**<br>
 `#M,NEXT*X4\r\n`
- **Select Course:**<br>
 `#C,SELECT,CourseName*B2\r\n`
- **Recommend Sail Event:**<br>
 `#S,A,J1*34\r\n`

---

For an up-to-date list of ALL control/status commands, always refer to your app's UDPListener implementation and, where possible, the latest Expedition Marine documentation.
