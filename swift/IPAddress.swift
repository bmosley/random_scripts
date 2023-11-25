//
//  IPAddress.swift
//
//  Created by Bryan Mosley on 12/9/20.
//

import Foundation
import RegexBuilder

func localIPAddresses() -> [String] {

    // let searchIPv4 = /(\d+).(\d+).(\d+).(\d+)/
    // experimenting with builder
    let searchIPv4 = Regex {
        Capture {
            OneOrMore(.digit)
        }
        "."
        Capture {
            OneOrMore(.digit)
        }
        "."
        Capture {
            OneOrMore(.digit)
        }
        "."
        Capture {
            OneOrMore(.digit)
        }
    }

    let interfaceTypes: [String] = ["en0", "en1", "ipsec0"]
    var addrList: UnsafeMutablePointer<ifaddrs>?

    var availableAddresses: [String] = []

    guard
        getifaddrs(&addrList) == 0,
        let firstAddr = addrList
    else { return [] }
    defer { freeifaddrs(addrList) }

    for cursor in sequence(first: firstAddr, next: { $0.pointee.ifa_next }) {
        let interfaceName = String(cString: cursor.pointee.ifa_name)
        // ignore extra interface types
        if !interfaceTypes.contains(interfaceName) {
            continue
        }
        var hostname = [CChar](repeating: 0, count: Int(NI_MAXHOST))
        if let addr = cursor.pointee.ifa_addr,
           getnameinfo(addr, socklen_t(addr.pointee.sa_len),
                       &hostname,
                       socklen_t(hostname.count),
                       nil,
                       socklen_t(0),
                       NI_NUMERICHOST) == 0,
           hostname[0] != 0 {
            let addrStr = String(cString: hostname)
            if let result = try? searchIPv4.wholeMatch(in: addrStr) {
                availableAddresses.append("\(result.0)")
            } else {
                continue
            }
        }
    }
    return availableAddresses
}
